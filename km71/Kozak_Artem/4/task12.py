m_block = int(input(" Enter 'n' blocks count: "))
n_block = int(input(" Enter 'm' blocks count: "))
k_block = int(input(" Enter 'k' blocks count: "))
input(" YES") if (k_block % n_block == 0 and m_block - (k_block // n_block) >= 0) or  (k_block % m_block == 0 and n_block - (k_block // m_block) >= 0) else input(" NO")
