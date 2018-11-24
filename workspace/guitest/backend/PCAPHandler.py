import subprocess


class PCAPHandler:

    def __init__(self, dissector="tshark"):
        self.dissector = dissector

    def convert(self, pcap_file):
        pdml_file = 'output.pdml'
        command = self.dissector+' -2 -R "icmp||tcp||dns" -r '+pcap_file+' -T pdml > '+pdml_file
        subprocess.call(command, shell=True)

        return pdml_file

