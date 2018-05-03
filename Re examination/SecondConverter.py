"""SecondConverter"""
def main():
    """This code converts time by second"""
    k_sec = int(input())
    s_sec = int(input())
    m_min = int(input())
    h_hr = int(input())
    k_sec = k_sec % (h_hr*m_min*s_sec)
    hour = k_sec // (m_min*s_sec)
    k_sec = k_sec % (m_min*s_sec)
    minu = k_sec // (s_sec)
    k_sec = k_sec % (s_sec)
    sec = k_sec
    print("%d:%d:%d" %(hour, minu, sec), end="")
main()
