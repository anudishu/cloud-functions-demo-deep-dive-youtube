def hello(request):
    request_json = request.get_json()
    name = "Stranger"
    if request.args and "name" in request.args:
        name = request.args.get("name")
    elif request_json and "name" in request_json:
        name = request_json["name"]
    return f"Hello, {name}!!!"
    