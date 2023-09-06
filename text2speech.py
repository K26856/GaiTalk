from pathlib import Path
from voicevox_core import VoicevoxCore, METAS
import os

class Text2Speech :
    def __init__(self) :
        pass

    def tts(self, text, speaker_id) :
        pass

    def get_speaker_ids(self) :
        pass


class VoicevoxWrapper(Text2Speech) :
    def __init__(self) :
        self.core = VoicevoxCore(open_jtalk_dict_dir=Path("open_jtalk_dic_utf_8-1.11"))

    def tts(self, text, speaker_id) :
        if not self.core.is_model_loaded(speaker_id) :
            self.core.load_model(speaker_id)
        wave_bytes = self.core.tts(text, speaker_id)
        return wave_bytes

    def get_speaker_ids(self) :
        result = []
        for m in METAS :
            for s in m.styles :
                result.append({
                    'speaker_id' : s.id,
                    'speaker_name' : '{}({})'.format(m.name, s.name)
                })
        return result        