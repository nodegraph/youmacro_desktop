
class YDLProgress:
    def __init__(self, obj=None):
        if not obj:
            self.obj = {}
        else:
            self.obj = obj

    def update_obj(self, obj):
        self.obj = obj

    def get_status(self):
        if 'status' not in self.obj:
            return ''
        return self.obj['status']

    def get_filename(self):
        """Returns currently downloading media file.
        This can be audio only or video only or audio+video file."""
        if 'filename' not in self.obj:
            return ''
        return self.obj['filename']

    def get_temp_filename(self):
        """Returns the currently downloading multi-part file.
        These multi-part files will be combined into the target
        filename."""
        if 'tmpfilename' not in self.obj:
            return ''
        return self.obj['tmpfilename']

    def get_downloaded_bytes(self):
        if 'downloaded_bytes' not in self.obj:
            return 0
        return self.obj['downloaded_bytes']

    def get_total_bytes(self):
        if 'total_bytes' not in self.obj:
            return 0
        return self.obj['total_bytes']

    def get_eta(self):
        if 'eta' not in self.obj:
            return 0
        return self.obj['eta']

    def get_speed(self):
        if 'speed' not in self.obj:
            return 0.0
        return self.obj['speed']

    def get_elapsed(self):
        if 'elapsed' not in self.obj:
            return 0.0
        return self.obj['elapsed']

    def get_eta_string(self):
        if '_eta_str' not in self.obj:
            return '00:00'
        return self.obj['_eta_str']

    def get_percent_string(self):
        if '_percent_str' not in self.obj:
            return '0.0%'
        return self.obj['_percent_str']

    def get_speed_string(self):
        if '_speed_str' not in self.obj:
            return '0.0MiB/s'
        return self.obj['_speed_str']

    def get_total_bytes_string(self):
        if '_total_bytes_str' not in self.obj:
            return '0.0MiB'
        return self.obj['_total_bytes_str']