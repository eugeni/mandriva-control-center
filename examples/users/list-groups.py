import dbus
bus = dbus.SystemBus()
proxy = bus.get_object(
    'org.mandrivalinux.mcc2.Users',
    '/org/mandrivalinux/mcc2/Users')
interface = dbus.Interface(proxy, 'org.mandrivalinux.mcc2.Users')
for group in interface.ListGroups():
    print group