import scapy.all as scapy
import optparse

def get_user_input():
    parse_object=optparse.OptionParser()
    parse_object.add_option("-i","--ipadress",dest="ip_adress",help="Enter your ip")
    (user_input,arguments) = parse_object.parse_args()
    if not user_input.ip_adress:
        print("Enter your fucking IP")
    return user_input
def scan_my_networ(ip):
    arp_request_packet = scapy.ARP(pdst=ip)
    #scapy.ls(scapy.ARP())
    brodcast_packet = scapy.Ether(dst ="ff:ff:ff:ff:ff:ff")
    #scapy.ls(scapy.Ether())
    combined_packet = brodcast_packet/arp_request_packet
    (answered_list,unanswered_list)=scapy.srp(combined_packet,timeout=1)
    answered_list.summary()
user_ip_adress= get_user_input()
scan_my_networ(user_ip_adress.ip_adress)

print("Thanks for using my new app")
print("We are anonymous,"
      "good job ,mr.H4ck3r")