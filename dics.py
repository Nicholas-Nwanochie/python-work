monthConversions = {
    "Jan": "January",
    "Feb": "Febuary",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July" ,
    "Aug": "August" ,
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}
"Get feature"
print(monthConversions["Aug"])
print(monthConversions.get("Dec"))

"set a default value for the .get"


print(monthConversions.get("Luv", "Not a valid key"))
