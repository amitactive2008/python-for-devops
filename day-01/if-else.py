for i in range(5):
    env=input('Please provide Env Name: ')
    print(f'Env Name provided by user is {env}')
    if env=='prod':
        print('Not Allowed')
    elif env =='stg':
        print('Take backup and then do. ')
    elif env == 'qa':
        print('Please check with QA team 1st: ')
    else:
        print('You can proceeds. ')
