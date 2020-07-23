class Solution:
    def validIPAddress(self, IP: str) -> str:
        if len(ipv4 := IP.split('.')) == 4:
            if set(IP) - set('.0123456789'):
                return 'Neither'
            elif any(v == '' for v in ipv4):
                return 'Neither'
            elif any(len(v) > 1 and v[0] == '0' for v in ipv4):
                return 'Neither'
            elif any(int(v) > 255 for v in ipv4):
                return 'Neither'
            else:
                return 'IPv4'
        elif len(ipv6 := IP.lower().split(':')) == 8:
            if set(IP.lower()) - set(':0123456789abcdef'):
                return 'Neither'
            elif any(4 < len(v) or v == '' for v in ipv6):
                return 'Neither'
            else:
                return 'IPv6'
        else:
            return 'Neither'
