from . import config
import httpx


class YouTube:
    def __init__(self, client: str):
        self._client = None
        self.youtube_api = None
        
        if client == "ANDROID_YOUTUBE":
            self._client = config.ANDROID_YOUTUBE
            self.youtube_api = config.REFERER_YOUTUBE_MOBILE + "youtubei/v1/"
        
    
    async def search(self, query: str):
        
        params = {
            "query": query
        }
        result = await self._request("search", params)
        return await self.parse_youtube_search(result)
    
    
    
    
    async def _request(self, endpoint:str, params: dict):
        
        api_url = self.youtube_api + endpoint
        payload = {
            **self._client,
            **params
        }
        
        async with httpx.AsyncClient(timeout=20) as client:
            res = await client.post(
                api_url,
                json=payload
            )
            res.raise_for_status()
            return res.json()
    
    
        
    async def parse_youtube_search(self, data: dict):
        """
        Parses YouTube Music search/browse JSON.
        Returns a list of video dicts with proper fallbacks.
        """
    
        videoList = []
    
        # Get sectionListRenderer contents safely
        section_contents = (
            data.get("contents", {})
                .get("sectionListRenderer", {})
                .get("contents", [])
        )
    
        for section in section_contents:
            # Drill into itemSectionRenderer if present
            items = section.get("itemSectionRenderer", {}).get("contents", [])
            for item in items:
                # The video can be directly in compactVideoRenderer
                video = item.get("compactVideoRenderer")
                
                # Or nested inside elementRenderer → newElement → compactVideoRenderer (sometimes)
                if not video and "elementRenderer" in item:
                    element = item["elementRenderer"]
                    video = element.get("compactVideoRenderer")
                    # If still nothing, skip
                    if not video:
                        continue
    
                if not video:
                    continue
    
                # Video ID
                videoId = video.get("videoId")
    
                # Thumbnails
                thumbnails = video.get("thumbnail", {}).get("thumbnails", [])
                thumbnail_url = None
                if thumbnails:
                    # Try to get 480x360
                    thumbnail_url = next(
                        (t.get("url") for t in thumbnails if t.get("width") == 480 and t.get("height") == 360),
                        thumbnails[-1].get("url")  # fallback to last
                    )
    
                # Title
                title_runs = video.get("title", {}).get("runs", [])
                title = title_runs[0].get("text") if title_runs else None
    
                # Published Time
                published_runs = video.get("publishedTimeText", {}).get("runs", [])
                publishedTimeText = published_runs[0].get("text") if published_runs else None
    
                # Video Length
                length_runs = video.get("lengthText", {}).get("runs", [])
                lengthText = length_runs[0].get("text") if length_runs else None
    
                # Channel Thumbnail
                channel_thumbs = video.get("channelThumbnail", {}).get("thumbnails", [])
                channelThumbnail = channel_thumbs[0].get("url") if channel_thumbs else None
    
                # Short View Count
                view_runs = video.get("shortViewCountText", {}).get("runs", [])
                shortViewCountText = view_runs[0].get("text") if view_runs else None
    
                # Channel Name
                byline_runs = video.get("longBylineText", {}).get("runs", [])
                channelName = byline_runs[0].get("text") if byline_runs else None
    
                # Build dict
                videoData = {
                    "videoId": videoId,
                    "title": title,
                    "thumbnail": thumbnail_url,
                    "ViewsText": shortViewCountText,
                    "published": publishedTimeText,
                    "lengthText": lengthText,
                    "channelName": channelName,
                    "channelThumbnail": channelThumbnail
                }
    
                videoList.append(videoData)
    
        return videoList
        
                    
                        
                
                
            
            
                
            