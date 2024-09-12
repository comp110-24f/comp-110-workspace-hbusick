"""Booleans and Conditionals Lecture"""


def get_weather_report() -> None:
    weather = str(input("What is the weather?"))
    if weather == "rainy" or weather == "cold":
        print("Bring a jacket")
    elif weather == "hot":
        print("Keep it cool")
    else:
        print("Weather not recognized")
