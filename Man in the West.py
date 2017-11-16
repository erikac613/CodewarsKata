def check_the_bucket(bucket):
    for item in bucket:
        if item == 'gold':
            return True
    else:
        return False
