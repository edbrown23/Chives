import json

class ChivesMemory():
    def __init__(self):
        self.userGender = ""
        self.userName = ""

class ChivesMemoryEncoderDecoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ChivesMemory):
            return [obj.userGender, obj.userName]
        return json.JSONEncoder.default(self, obj)

    def as_chives_memory(self, dct):
        if '__ChivesMemory__':
            mem = ChivesMemory()
            mem.userGender = dct['userGender']
            mem.userName = dct['userName']
            return mem