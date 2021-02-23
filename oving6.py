import rsa  # tis the given file


# we want to find the two primes that the public and private keys are made out of (p & q)
def find_key_primes(n):
    primes = rsa.PrimeGen(1000)
    for p in primes:
        if n % p == 0:
            q = n // p
            yield p, q


def rsa_brutality(public_key, encrypted_message):
    try:
        e, n = public_key

        # using a generator to find possible primes then trying to decrypt the message
        for p, q in find_key_primes(n):
            phi = (p - 1) * (q - 1)
            d = rsa.multiplicative_inverse(e, phi)
            private_key = d, n
            decrypted_message = rsa.decrypt(private_key, encrypted_message)
            if decrypted_message.startswith('h'):
                return decrypted_message
    except:
        pass


if __name__ == '__main__':
    public_key = (29815, 100127)
    encrypted_message = [84620, 66174, 66174, 5926, 9175, 87925, 54744, 54744, 65916, 79243, 39613, 9932, 70186, 85020,
                         70186, 5926, 65916, 72060, 70186, 21706, 39613,
                         11245, 34694, 13934, 54744, 9932, 70186, 85020, 70186, 54744, 81444, 32170, 53121, 81327,
                         82327, 92023, 34694, 54896, 5926, 66174, 11245, 9175,
                         54896, 9175, 66174, 65916, 43579, 64029, 34496, 53121, 66174, 66174, 21706, 92023, 85020, 9175,
                         81327, 21706, 13934, 21706, 70186, 79243, 9175,
                         66174, 81327, 5926, 74450, 21706, 70186, 79243, 81327, 81444, 32170, 53121]

    print(rsa_brutality(public_key, encrypted_message))
