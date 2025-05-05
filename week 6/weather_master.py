"""
File: weather_master.py
Name: Polly
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
EXIT = -100


def main():
	print('stanCode "Weather Master 4.0"!')
	enter = int(input("Next Temperature: (or -100 to quit)? "))

	if enter == EXIT:
		print("No temperatures were entered.")
	else:
		maximum = enter
		minimum = enter
		cold_counter = 0
		counter = 0
		sum = 0
		#highest #lowest #average #cold alarm
		while enter != EXIT:
			sum = sum + enter
			counter += 1
			if enter < 16:
				cold_counter += 1
			if enter > maximum:
				maximum = enter
			if enter < minimum:
				minimum = enter

			enter = int(input("Next Temperature: (or -100 to quit)? "))
		print("Highest temperature =", maximum)
		print("lowest temperature =", minimum)
		print("Average =", sum/counter)
		print(cold_counter, "cold day(s)")










"""
	if guess_temperature == EXIT:
		print("No temperatures were entered.")
	else:
		maximum_temperature = guess_temperature
		minimum_temperature = guess_temperature
		total_temperature_sum = guess_temperature
		cold_alarm_box = guess_temperature



		# maximum temperature
		while guess_temperature != EXIT:
			if maximum_temperature < guess_temperature:
				maximum_temperature = guess_temperature
			guess_temperature = int(input("Next Temperature: (or -100 to quit)? "))
		print("Highest temperature =", maximum_temperature)


		# minimum temperature
		while guess_temperature != EXIT:
			if minimum_temperature > guess_temperature:
				minimum_temperature = guess_temperature
			guess_temperature = int(input("Next Temperature: (or -100 to quit)? "))
		print("Lowest temperature =", minimum_temperature)

		#cold alarm
		while guess_temperature != EXIT:
			counter = 0
			cold_alarm_counter = 0
			if cold_alarm_box < 16:
				cold_alarm_counter += 1
			guess_temperature = int(input("Next Temperature: (or -100 to quit)? "))
		print(str(counter), "cold day(s)")

		#average temperature
		while guess_temperature != EXIT:
			counter = 0
			total_temperature_sum = total_temperature_sum + guess_temperature
			counter = counter + 1
			guess_temperature = int(input("Next Temperature: (or -100 to quit)? "))
		average = total_temperature_sum
		print("Average =", str(average))
"""


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
