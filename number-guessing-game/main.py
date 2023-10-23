class GuessingGame:
    def __init__(self, answer: int, min: int = 0, max: int = 30) -> None:
        self._answer = answer
        self._min = min
        self._max = max
        self._guess = 0
        
    def reset_guess_count(self) -> None:
        self._guess = 0
        
    def get_guess(self) -> int:
        self._guess += 1
        
        guess = input(f'Guess the number between {self._min} - {self._max}: ')
        
        valid, answer = self.validate_answer(guess)
        
        if not valid:
            print('Invalid Answer!')
            return self.get_guess()
        
        return answer 
    
    def validate_answer(self, answer: str) -> (bool, int):
        try:
            num = int(answer)
            
        except:
            return False, -1
            
        return self._min <= num <= self._max, num
        
    def play(self) -> None:
        self.reset_guess_count()
        
        while True:            
            answer = self.get_guess()
            
            if answer > self._answer:
                print('Your guess was over.')
                
            elif answer < self._answer:
                print('Your guess was under.')
                
            else:
                break
        
        print(f'You got the answer within {self._guess} guess.')
        
        
def main() -> None:
    game = GuessingGame(12)
    
    game.play()
    
    
if __name__ == '__main__':
    main()
