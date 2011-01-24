import dbus
bus = dbus.SystemBus()
proxy = bus.get_object(
    'com.mandriva.mcc2.SystemServices',
    '/com/mandriva/mcc2/SystemServices')
interface = dbus.Interface(proxy, 'com.mandriva.mcc2.SystemServices')
for service in interface.list():
    for s in service:
        print s
    print '-'*80