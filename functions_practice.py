# function tripler(array) {
#   const arr = [];
#
#   for ( i = 0; i < array.length; i += 1) {
#     let num = array[i];
#     arr.push(num * 3);
#   }
#
#   return arr;
# }
def tripler(arr):
    result = []
    for i in range(len(arr)):
        num = arr[i]
        multiple = num * 3
        result.append(multiple)
    return result

print(tripler([1,6,244,5,60]))
# function oddRange(end) {
#   const arr = [];
#
#   for (let i = 1; i <= end; i += 2) {
#       arr.push(i);
#   }
#
#   return arr;
# }

def add_range(end):
    arr = []
    for i in range(len(end)):
        arr.push[i]

# // solution 1
# function catBuilder(name, color, toys) {
#   const cat = {
#     name: name,
#     color: color,
#     toys: toys
#   };
#
#   return cat;
# }

#   // solution 2
# function catBuilder(name, color, toys) {
#   const cat = {};
#
#   cat.name = name;
#   cat.color = color;
#   cat.toys = toys;
#
#   return cat;
# }

# function valuePair(obj1, obj2, key) {
#     let val1 = obj1[key];
#     let val2 = obj2[key];
#     const arr = [val1, val2];
#
#     return arr;
# }
#
# function doesKeyExist(obj, key) {
#   return obj[key] !== undefined;
# }
#
# function adults(people) {
#   const names = [];
#
#   for (let i = 0; i < people.length; i += 1) {
#     let person = people[i];
#     if (person.age >= 18) {
#       names.push(person.name);
#     }
#   }
#
#   return names;
# }
#
# function adults(people) {
#     const names = [];
#
#     for (let i = 0; i < people.length; i += 1) {
#       let person = people[i];
#       if (person.age >= 18) {
#         names.push(person.name);
#       }
#     }
#
#     return names;
# }
#
# /***********************************************************************
# In these exercises we will be practicing decomposition by building
# multiple functions. Be sure to test each function thoroughly as you go
# before moving on to the next problem. Each function will require the
# previous to solve.
# ***********************************************************************/
#
#
# /***********************************************************************
# Write a function `isPrime(number)` that returns a boolean indicating if
# `number` is prime or not. Assume `number` is a positive integer.
# Examples:
# isPrime(2); // => true
# isPrime(1693); // => true
# isPrime(15); // => false
# isPrime(303212); // => false
# ***********************************************************************/
#
# function isPrime(number) {
#     if (number < 2) {
#       return false;
#     }
#
#     for (let i = 2; i < number; i += 1) {
#       if (number % i === 0) {
#         return false;
#       }
#     }
#
#     return true;
# }
#
#   /***********************************************************************
#   Using the `isPrime` function you made, write a function `firstNPrimes(n)`
#   that returns an array of the first `n` prime numbers.
#
#   Examples:
#
#   firstNPrimes(0); // => []
#   firstNPrimes(1); // => [2]
#   firstNPrimes(4); // => [2, 3, 5, 7]
#   ***********************************************************************/
#
# function firstNPrimes(n) {
#     const primes = [];
#     let num = 2;
#
#     while(primes.length < n) {
#       if (isPrime(num)) {
#         primes.push(num);
#       }
#
#       num += 1;
#     }
#
#     return primes;
# }
#
# /***********************************************************************
#  Using `firstNPrimes`, write a function `sumOfNPrimes(n)` that returns
# the sum of the first `n` prime numbers.
# Examples:
# sumOfNPrimes(0); // => 0
# sumOfNPrimes(1); // => 2
# sumOfNPrimes(4); // => 17
# ***********************************************************************/
#
# function sumOfNPrimes(n) {
#   let sum = 0;
#   let primes = firstNPrimes(n);
#
#   for (let i = 0;  i < primes.length; i += 1) {
#       sum += primes[i];
#   }
#
#   return sum;
# }
#
#
# /***********************************************************************
# Write a function `countScores(people)` that takes in an array of score
# objects (people) as its input. A score object has two key-value pairs:
# a name (string) and a score (number). `countScores(people)` should
# return an object that has key-value pairs where each name is a key and
# the value is their total score.
# Example 1
# const ppl = [ {name: "Pete", score: 10},
#             {name: "Mike", score : 10},
#             {name: "Pete", score: -8},
#             {name: "Dexter", score: 12}];
# let countPpl = countScores(ppl);
# countPpl; //=> { Pete: 2, Mike: 10, Dexter: 12 }
# Example 2
# const peeps = [
#   {name: "Pete", score: 2},
#   {name: "Dexter", score: 2},
#   {name: "Mike", score: 2},
#   {name: "Dexter", score: 2},
#   {name: "Mike", score: 2},
#   {name: "Pete", score: 2},
#   {name: "Dexter", score: 2}
# ];
# countScores(peeps); //=> { Pete: 4, Mike: 4, Dexter: 6 }
# ***********************************************************************/
#
#
# function countScores(people) {
#   const scoresObj = {};
#
#   for (let i = 0; i < people.length; i += 1) {
#     let personObj = people[i];
#     let name = personObj.name;
#     let score = personObj.score;
#
#     if (scoresObj[name]) {
#       scoresObj[name] += score;
#     } else {
#       scoresObj[name] = score;
#     }
#   }
#
#   return scoresObj;
# }
