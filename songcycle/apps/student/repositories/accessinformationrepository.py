# import area
from student.models.accessinformation import AccessInformation

# CRUDのCUDは、ここに集約する。

def insert(event_type, http_accept_language, browser, browser_version, os, os_version, device, device_brand, device_type, 
remote_addr, success_value, fault_value, comment):
    
    access_information = AccessInformation(
        event_type = event_type,
        http_accept_language = http_accept_language,
        browser = browser,
        browser_version = browser_version,
        os = os,
        os_version = os_version,
        device = device,
        device_brand = device_brand,
        device_type = device_type,
        remote_addr = remote_addr, 
        success_value = success_value,
        fault_value = fault_value,
        comment = comment
    )

    access_information.save()
