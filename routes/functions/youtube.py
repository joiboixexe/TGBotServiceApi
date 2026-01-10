from flask import request, jsonify
from config import Clients, BOT_TOKEN
from module import TelegramMiniApp, YouTube



bot_token = BOT_TOKEN

async def handle():
    """
    Async auth handler for /api/browse
    """
    # Get query parameters
    body = request.get_json(silent=True) or {}
    
    headers = request.headers
    initData = headers.get("Authorization", None)
    clientName = body.get("context", {}).get("clientName", None)
    query = body.get("query", None)
    
    if not query or not initData or not clientName or not clientName==Clients.miniapp:
        return jsonify(
            status=False,
            error="Invalid request"
        ), 400
    
    try:
        data = TelegramMiniApp.verify_init_data(initData)   
    except Exception as e:
        return jsonify(
            status= False,
            error= f"{e}"
        ) 
    
    client = YouTube("ANDROID_YOUTUBE")
    
    result = await client.search(query)
        
        
    # Return JSON response
    return jsonify(
        result
    )
    
