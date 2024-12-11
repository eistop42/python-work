def pam(count):
    count += 1
    if count == 300:
        return count
    print(f'привет {count}')
    pam(count)

pam(2)