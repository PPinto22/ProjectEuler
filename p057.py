if __name__ == '__main__':
    results = []
    n = 3
    d = 2
    for i in range(0,1000):
        n = n + 2*d
        d = n - d
        if len(str(n)) > len(str(d)):
            results.append((n,d))
    print results
    print len(results)