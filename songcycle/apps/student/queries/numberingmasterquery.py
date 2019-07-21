import threading

from apps.student.models.numberingmaster import NumberingMaster


class NumberingMasterQuery:

    __singleton = None
    __new_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        cls.__new_lock.acquire()
        if cls.__singleton is None:
            cls.__singleton = super(NumberingMasterQuery, cls).__new__(cls)
        cls.__new_lock.release()
        return cls.__singleton

    def get_report_id(self):

        master = NumberingMaster.objects.filter(code="02").first()
        report_id = master.initial + str(master.value).zfill(6)

        master.value += 1
        NumberingMaster.save(master)

        return report_id

    def get_user_id(self):
    
        master = NumberingMaster.objects.filter(code="01").first()
        user_id = master.initial + str(master.value).zfill(4)

        master.value += 1
        NumberingMaster.save(master)

        return user_id
