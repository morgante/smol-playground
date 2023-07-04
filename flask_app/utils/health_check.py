def health_check():
    try:
        # Here you can add any system health check logic
        # For simplicity, we will just return a static response
        return {"status": "OK", "message": "System is healthy"}
    except Exception as e:
        return {"status": "ERROR", "message": str(e)}