# Examples

Everyone likes some short bits of code to taste the syntax and semantics.

For more in depth code examples and explaination, check the feature pages.

!!! warning
	Some of the examples shown below are non-functional. Please consult the rest of the documentation for more information

```py
# Hello World
print('Hello World')
print('🍌')
print('夜のコンサートは最高でした。')

a_number: int # Initialize an Integer

π = 3.14 # Support for utf-8 variable names
number = 23 # Type Inference, int in this case
number = number + 5 // 2 ^ 3 # Number operations
number+=5 # Operating Assignment
number//=3

question = 'what\'s going on' # Escaping

things = [1, 2, 3] # Array, homogeneous
other_things = (1, 'Hello') # List, non-homogeneous
stuff = {'first_name': 'Samus', 'last_name': 'Aran'} # Dictionary
other_stuff: int[] = [] # Empty Array of Ints

print(things[1 + 1])

if number > 23
	print('greater than 23')
else if number == 23
	print('equals 23')
else
	print('less than 23')

if something is not number \ # Continuing statement onto next line
		and true # Indentaion requires tabs only
	print('They are not the same')

for x in 0..40 # For loop using a range
	print(x * 2)

for item in things # Iterate over objects
	print(item)

while number > 1
	number -= 1
	print(number)

if 2 in things
	print('yes')

if 2 not in things
	print('no')

special_num = 1

switch special_num
	case 1
		print('Number one')
	case 2
		print('Number two')
		break
	default
		print("Big number")
		print(special_num)
	case 3
		print('Number three')

# Function Return notation
def fib(n: int) -> int
	a = 0
	b = 1
	for _ in 0..n
		prev_a = a
		a = b
		b = prev_a + b
	return a

def fib_rec(n: int) -> int
	if n == 0
		return 0
	if n == 1
		return 1
	return fib_rec(n - 1) + fib_rec(n - 2)

def factorial(n: int = 5) -> int
	if n <= 1
		return 1
	return n * factorial(n - 1)

# Assign anonymous function to a variable
myfunc = def (x: int, y: int) -> int
	if x > y
		return x + y
	else
		return x * y

print(myfunc(2, 3))
bar = myfunc
print(bar(3,4))


# Type Aliasing
type fInt = func[int] -> int

def do_stuff(x: int, callback: fInt) -> int
	x ^= 2
	x = callback(x)
	return x

num = do_stuff(3,
	def (y: int) -> int
		y += 7
		return y
)

print(
	num
)

# Closure
def start_at(x: int) -> fInt
	def increment_by(y: int) -> int
		return x + y
	return increment_by

start_at_5 = start_at(5)
start_at_27 = start_at(27)

print(start_at_5(4))
print(start_at_27(15))

# User input
Int age = input('How old are you?')

# String Interpolation
print('Wow! You are {age} years old?!')

enum Colors
	GREEN
	RED
	BLUE
	YELLOW


struct Circle
	radius: int
	x: int
	y: int

cir: Circle = {radius=5, x=2, y=4}

print(cir.radius)

class Vehicle
	# Constructor
	new(year: int, color: str)
		this.year = year
		this._color = color

# Inheritance
class Car(Vehicle)
	new(year: int, color='green', hatchback=false)
		this.hatchback = hatchback
		super.Vehicle(year, color)

	print_year() -> void
		print('This car was made in {this.year}')

ford = Car(1992)

print(ford.hatchback)
```