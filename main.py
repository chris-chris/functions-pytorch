# PATH = "model.pth"


class TranslateModel:
    def predict(message):
        return message + " translated"

    def load_state_dict(path):
        pass


def translate_pytorch(request):
    request_json = request.get_json()
    model = TranslateModel()
    model.load_state_dict("torch.load(PATH)")  # torch.load(PATH)

    if request_json and 'message' in request_json:
        message = request_json['message']
        # message 전처리
        result = model.predict(message)
        return {
            "code": 200,
            "message": "OK",
            "data": result
        }, 200
    else:
        return {
            "code": 400,
            "message": "No message found",
            "data": None
        }, 400
    return True
