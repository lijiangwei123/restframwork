import time
VISIT_RECORD = {}
class Visit(object):
    def __init__(self):
        self.history = None

    def allow_request(self, request, view):
        # 获取用户的ip,通过ip记录用户的请求
        remote_addr = request.META.get('REMOTE_ADDR')
        ctime = time.time()
        if remote_addr not in VISIT_RECORD:
            VISIT_RECORD[remote_addr] = [ctime, ]
            return  True
        history = VISIT_RECORD.get(remote_addr)
        self.history = history
        while history and history[-1] < ctime - 30:
            history.pop()

        if(len(history) < 3):
            history.insert(0, ctime)
            return True


    def wait(self):
        ctime = time.time()
        wait_time = 30 - (ctime - self.history[-1])
        return  wait_time