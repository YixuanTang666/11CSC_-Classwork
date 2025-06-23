
subjects = ['11CSC','11PSY']
for subject in subjects:
    print(subject)
while True:
    new_subject = input('Enter a new subject: ')
    if new_subject == 'done':
        break
    subjects.append(new_subject.title()) 
subjects.sort()
for subject in subjects:
    print(subject)