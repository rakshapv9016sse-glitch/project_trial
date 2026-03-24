text = input("Enter a String:");
m_char = "";
m_count = 0;
for ch in text:
    count = text.count(ch)
    if count > m_count:
        m_count = count 
        m_char = ch
print("most fre char:", m_char)
print("no of time",m_count)