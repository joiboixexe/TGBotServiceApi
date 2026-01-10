from flask import request, jsonify
from config import Clients, BOT_TOKEN
from module import TelegramMiniApp



bot_token = BOT_TOKEN

def handle():
    """
    Async auth handler for /api/auth
    """
    # Get query parameters
    body = request.get_json(silent=True) or {}
    
    initData = body.get("initData", None)
    clientName = body.get("context", {}).get("clientName", None)
    
    if not initData or not clientName or not clientName==Clients.miniapp:
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
        
    # Return JSON response
    return jsonify(
        status= True,
        verified= True
    )
    


    

