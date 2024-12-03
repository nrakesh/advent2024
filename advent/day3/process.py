import re


def read_file_content(filename):
  try:
    with open(filename, 'r') as file:
      content = file.read()
    return content
  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
    return None

def get_sum(matches):
    sum = 0
    for match in matches:
        num1, num2 = match
        #print(f"Found mul({num1},{num2})")
        sum += int(num1) * int(num2)
    #print(f"Sum = {sum}")
    return sum

f="2024-3-input.txt"
f1="test.txt"
text = read_file_content(f)
text = text.replace('\n', '').replace('\r', '')
# Define the regular expression pattern
pattern1 = r"mul\((\d+),(\d+)\)"
pattern2 = r"don't\(\)(.*?)(?=do\(\))"



# Find all matches in the text
matches = re.findall(pattern1, text)
sum1 = get_sum(matches)

matches2 = re.findall(pattern2, text)
sum2 = 0
for match in matches2:
    print(match)
    m = re.findall(pattern1, match)
    sum2 += get_sum(m)

print(f"Sum2 = {sum2}")
total = sum1-sum2
print(total)



