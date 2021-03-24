/*
  ! Due to limitation in Javascript This script can't compute Big Numbers
  @author :Badr4u
 */

interface Public_Key {
  n: number;
  e: number;
}
interface Private_Key {
  n: number;
  d: number;
}
interface General_Key {
  Public_Key: Public_Key;
  Private_Key: Private_Key;
}

class RSA_KEY {
  isPrime(num: number) {
    for (let index = 2; index < num; index++) {
      if (num % index === 0) {
        return { status: false };
      }
    }
    return { status: true, num };
  }
  Random_Numb_init(limit: number): number {
    return Math.floor(Math.random() * limit + 10);
  }
  Random_Numb(limit: number): number {
    return Math.floor(Math.random() * limit);
  }
  Generate_Keys(): General_Key {
    const Numbers: number[] = [];
    while (Numbers.length < 2) {
      let Rand = this.Random_Numb_init(50);
      if (this.isPrime(Rand).status === true) {
        Numbers.push(Rand);
      }
    }
    console.log("My 2 Numbers :", Numbers);
    const n = Numbers[0] * Numbers[1];
    const q = (Numbers[0] - 1) * (Numbers[1] - 1);
    let e = 0;
    for (let i = 2; i > 0; i++) {
      if (this.gcd(i, q) == 1) {
        console.log("Find e", i);
        e = i;
        break;
      }
    }

    let d = 0;
    for (let i = 1; i > 0; i++) {
      if (Number.isInteger((q * i + 1) / e)) {
        console.log("Find d", (q * i + 1) / e);
        d = (q * i + 1) / e;
        break;
      }
    }

    const Public_Key = { n, e };
    const Private_Key = { d, n };
    return { Public_Key, Private_Key };
  }
  gcd = (a: number, b: number): number => {
    if (!b) {
      return a;
    }

    return this.gcd(b, a % b);
  };
}
const Encrypt = (Message: number, Public: Public_Key): number => {
  /*
  ! If Message is a string you must Convert to ascii Number 
  let num = "";
  for (let index = 0; index < Message.length; index++) {
    num += Message.charCodeAt(index);
  }
  console.log("Number of ascii", num);
  */

  return Math.pow(Message, Public.e) % Public.n;
};
const Decrypt = (message_cry: number, Private: Private_Key): number => {
  return Math.pow(message_cry, Private.d) % Private.n;
};

const Keys = new RSA_KEY();

const key = Keys.Generate_Keys();
console.log(key);
const Private_Message = Encrypt(2, key.Public_Key);
console.log("Numero Crypté", Private_Message);
const Public_Message = Decrypt(Private_Message, key.Private_Key);
console.log("Numéro décrypter", Public_Message);
