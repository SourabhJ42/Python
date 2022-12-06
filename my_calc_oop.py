class MyOOPSCalculator:

    def __init__(self, rcv_first_num, rcv_second_num=1):
        self.first_num = rcv_first_num
        self.second_num = rcv_second_num

    def my_addition(self):
        return self.first_num + self.second_num

    def my_square(self):
        """ receives two numbers from the invoking application and returns first number squared 2"""
        return str(self.first_num ** 2)

    def my_exponenation(self):
        return self.first_num ** self.second_num

    @classmethod
    def my_calculator(cls):
        print("****************** MENU ************************")
        print("1: Addition")
        print("2: Square")
        print("3: Exponentation ")
        choice = int(input("Please select your choice"))

        match choice:
            case 1:
                my_cal_add_object = MyOOPSCalculator(int(input("Please enter First number:")),
                                                     int(input("Please enter Second number:")))
                print("The Addition of the numbers is ", my_cal_add_object.my_addition())

            case 2:
                my_cal_sqr_object = MyOOPSCalculator(int(input("Please enter First number:")))
                print("The Square of the number is ", my_cal_sqr_object.my_square())

            case 3:
                my_cal_exp_object = MyOOPSCalculator(int(input("Please enter First number:")),
                                                     int(input("Please enter Second number:")))
                print("The exponenation of the numbers is ", my_cal_exp_object.my_exponenation())

    @staticmethod
    def iterative_calculator():
        while True:
            print("Lets start !!!! ")
            MyOOPSCalculator.my_calculator()
            choice = input("\nDo you want to continue (Y/N):: ").lower()
            if choice == 'n':
                break


MyOOPSCalculator.iterative_calculator()
