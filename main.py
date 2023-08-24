from tkinter import *
from functions import *


# functionality part
def total():
    soap = int(bathSoupEntry.get()) * 30
    faceCream = int(faceCreamEntry.get()) * 40
    faceWash = int(faceWashEntry.get()) * 80
    hairSpray = int(hairSprayEntry.get()) * 55
    hairgel = int(hairGelEntry.get()) * 23
    bodyLotion = int(bodyLotionEntry.get()) * 45

    totalCosPrice = soap + faceCream + faceWash + hairSpray + hairgel + bodyLotion
    cosmeticPriceEntry.delete(0, END)
    cosmeticPriceEntry.insert(
        0, str(totalCosPrice) + " Rs"
    )  # 0 indicates index of where to insert
    cosmeticTax = totalCosPrice * 0.15
    cosmeticTaxEntry.delete(0, END)
    cosmeticTaxEntry.insert(0, str(cosmeticTax) + "Rs")

    rice = int(riceEntry.get()) * 100
    oil = int(oilEntry.get()) * 180
    daal = int(daalEntry.get()) * 150
    wheat = int(wheatEntry.get()) * 120
    sugar = int(sugarEntry.get()) * 200
    tea = int(teaEntry.get()) * 100

    totalGroceryPrice = rice + oil + daal + wheat + sugar + tea
    groceryPriceEntry.delete(0, END)
    groceryPriceEntry.insert(0, str(totalGroceryPrice) + " Rs")
    groceryTax = totalGroceryPrice * 0.05
    groceryTaxEntry.delete(0, END)
    groceryTaxEntry.insert(0, str(groceryTax) + "Rs")

    maaza = int(maazaEntry.get()) * 50
    pepsi = int(pepsiEntry.get()) * 50
    sprite = int(spriteEntry.get()) * 50
    dew = int(dewEntry.get()) * 50
    frooti = int(frootiEntry.get()) * 50
    coca = int(cocaColaEntry.get()) * 50

    totalDrinkPrice = maaza + pepsi + sprite + dew + frooti + coca
    coolDrinkPriceEntry.delete(0, END)
    coolDrinkPriceEntry.insert(0, str(totalDrinkPrice) + " Rs")
    coolDrinkTax = totalDrinkPrice * 0.1
    coolDrinkTaxEntry.delete(0, END)
    coolDrinkTaxEntry.insert(0, str(coolDrinkTax) + "Rs")


# GUI part


root = Tk()
root.title("Retail Billing System")
# root.geometry("1270x675+0+0")
root.iconbitmap("bill_120383.ico")
root.state("zoomed")

headingLabel = Label(
    root,
    text="Retail Billing System",
    font=("times new roman", 30, "bold"),
    bg="gray20",
    fg="gold",
    bd=12,
    relief=GROOVE,  # for border styling
)
headingLabel.pack(fill=X, pady=2)  # fill the entire width label

# custor details frame
customDeFrame = LabelFrame(
    root,
    text="Customer Details",
    font=("times new roman", 15, "bold"),
    fg="gold",
    bd=8,
    bg="gray20",
    relief=GROOVE,
)  # only you can see this after adding contents
customDeFrame.pack(fill=X, pady=4)

nameLabel = Label(
    customDeFrame,
    text="Name",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
nameLabel.grid(row=0, column=0, padx=20)

nameEntry = Entry(customDeFrame, font=("arial", 15), bd=7, width=18)
nameEntry.grid(row=0, column=1, padx=8)

phoneLabel = Label(
    customDeFrame,
    text="Phone Number",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
phoneLabel.grid(row=0, column=2, padx=20)

phoneEntry = Entry(customDeFrame, font=("arial", 15), bd=7, width=18)
phoneEntry.grid(row=0, column=3, padx=8)

billNumLabel = Label(
    customDeFrame,
    text="Bill Number",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
billNumLabel.grid(row=0, column=4, padx=20)

billNumEntry = Entry(customDeFrame, font=("arial", 15), bd=7, width=18)
billNumEntry.grid(row=0, column=5, padx=8)

searchButton = Button(
    customDeFrame, text="SEARCH", font=("arial", 12, "bold"), bd=7, width=10
)
searchButton.grid(row=0, column=6, padx=20, pady=8)

productFrame = Frame(root)
# diff btw frame and label frame class is frame does not have a label but label frame have label

productFrame.pack(fill=X, pady=4)  # pack simply pack everything one after another

cosmeticsFrame = LabelFrame(
    productFrame,
    text="Cosmetics",
    font=("times new roman", 15, "bold"),
    fg="gold",
    bd=8,
    bg="gray20",
    relief=GROOVE,
)
cosmeticsFrame.grid(row=0, column=0)

bathSoupLabel = Label(
    cosmeticsFrame,
    text="Bath Soup",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
bathSoupLabel.grid(sticky="w", row=0, column=0, padx=8, pady=5)

bathSoupEntry = Entry(cosmeticsFrame, font=("arial", 15), bd=7, width=10)
bathSoupEntry.grid(row=0, column=1, padx=10, pady=5, sticky="w")
bathSoupEntry.insert(
    0, 0
)  # to avoid string literal error when a null is converted into int

faceCreamLabel = Label(
    cosmeticsFrame,
    text="Face Cream",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
faceCreamLabel.grid(row=1, column=0, padx=10, pady=5)

faceCreamEntry = Entry(cosmeticsFrame, font=("arial", 15), bd=7, width=10)
faceCreamEntry.grid(sticky="w", row=1, column=1, padx=10, pady=5)
faceCreamEntry.insert(0, 0)

faceWashLabel = Label(
    cosmeticsFrame,
    text="Face Wash",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
faceWashLabel.grid(sticky="w", row=2, column=0, padx=10, pady=5)

faceWashEntry = Entry(cosmeticsFrame, font=("arial", 15), bd=7, width=10)
faceWashEntry.grid(row=2, column=1, padx=8, pady=5, sticky="w")
faceWashEntry.insert(0, 0)

hairSprayLabel = Label(
    cosmeticsFrame,
    text="Hair Spray",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
hairSprayLabel.grid(sticky="w", row=3, column=0, padx=10, pady=5)

hairSprayEntry = Entry(cosmeticsFrame, font=("arial", 15), bd=7, width=10)
hairSprayEntry.grid(row=3, column=1, padx=8, pady=5)
hairSprayEntry.insert(0, 0)

hairGelLabel = Label(
    cosmeticsFrame,
    text="Hair Gel",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
hairGelLabel.grid(sticky="w", row=4, column=0, padx=10, pady=5)

hairGelEntry = Entry(cosmeticsFrame, font=("arial", 15), bd=7, width=10)
hairGelEntry.grid(row=4, column=1, padx=10, pady=5)
hairGelEntry.insert(0, 0)

bodyLotionLabel = Label(
    cosmeticsFrame,
    text="Body Lotion",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
bodyLotionLabel.grid(sticky="w", row=5, column=0, padx=10, pady=5)

bodyLotionEntry = Entry(cosmeticsFrame, font=("arial", 15), bd=7, width=10)
bodyLotionEntry.grid(row=5, column=1, padx=10, pady=5)
bodyLotionEntry.insert(0, 0)

groceryFrame = LabelFrame(
    productFrame,
    text="Grocery",
    font=("times new roman", 15, "bold"),
    fg="gold",
    bd=8,
    bg="gray20",
    relief=GROOVE,
)
groceryFrame.grid(row=0, column=1)

riceLabel = Label(
    groceryFrame,
    text="Rice",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
riceLabel.grid(sticky="w", row=0, column=0, padx=10, pady=5)

riceEntry = Entry(groceryFrame, font=("arial", 15), bd=7, width=10)
riceEntry.grid(row=0, column=1, padx=10, pady=5, sticky="w")
riceEntry.insert(0, 0)

oilLabel = Label(
    groceryFrame,
    text="Oil",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
oilLabel.grid(sticky="w", row=1, column=0, padx=10, pady=5)

oilEntry = Entry(groceryFrame, font=("arial", 15), bd=7, width=10)
oilEntry.grid(row=1, column=1, padx=10, pady=5)
oilEntry.insert(0, 0)

daalLabel = Label(
    groceryFrame,
    text="Daal",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
daalLabel.grid(sticky="w", row=2, column=0, padx=10, pady=5)

daalEntry = Entry(groceryFrame, font=("arial", 15), bd=7, width=10)
daalEntry.grid(row=2, column=1, padx=10, pady=5, sticky="w")
daalEntry.insert(0, 0)

wheatLabel = Label(
    groceryFrame,
    text="Wheat",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
wheatLabel.grid(sticky="w", row=3, column=0, padx=10, pady=5)

wheatEntry = Entry(groceryFrame, font=("arial", 15), bd=7, width=10)
wheatEntry.grid(row=3, column=1, padx=10, pady=5)
wheatEntry.insert(0, 0)

sugarLabel = Label(
    groceryFrame,
    text="Sugar",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
sugarLabel.grid(sticky="w", row=4, column=0, padx=10, pady=5)

sugarEntry = Entry(groceryFrame, font=("arial", 15), bd=7, width=10)
sugarEntry.grid(row=4, column=1, padx=10, pady=5)
sugarEntry.insert(0, 0)

teaLabel = Label(
    groceryFrame,
    text="Tea",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
teaLabel.grid(sticky="w", row=5, column=0, padx=10, pady=5)

teaEntry = Entry(groceryFrame, font=("arial", 15), bd=7, width=10)
teaEntry.grid(row=5, column=1, padx=10, pady=5)
teaEntry.insert(0, 0)

coolDrinkFrame = LabelFrame(
    productFrame,
    text="Cool Drinks",
    font=("times new roman", 15, "bold"),
    fg="gold",
    bd=8,
    bg="gray20",
    relief=GROOVE,
)

coolDrinkFrame.grid(row=0, column=2)

maazaLabel = Label(
    coolDrinkFrame,
    text="Maaza",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
maazaLabel.grid(sticky="w", row=0, column=0, padx=10, pady=5)

maazaEntry = Entry(coolDrinkFrame, font=("arial", 15), bd=7, width=10)
maazaEntry.grid(row=0, column=1, padx=10, pady=5, sticky="w")
maazaEntry.insert(0, 0)

pepsiLabel = Label(
    coolDrinkFrame,
    text="Pepsi",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
pepsiLabel.grid(row=1, column=0, padx=10, pady=5, sticky="w")

pepsiEntry = Entry(coolDrinkFrame, font=("arial", 15), bd=7, width=10)
pepsiEntry.grid(row=1, column=1, padx=10, pady=5)
pepsiEntry.insert(0, 0)

spriteLabel = Label(
    coolDrinkFrame,
    text="Sprite",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
spriteLabel.grid(sticky="w", row=2, column=0, padx=10, pady=5)

spriteEntry = Entry(coolDrinkFrame, font=("arial", 15), bd=7, width=10)
spriteEntry.grid(row=2, column=1, padx=10, pady=5, sticky="w")
spriteEntry.insert(0, 0)

dewLabel = Label(
    coolDrinkFrame,
    text="Dew",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
dewLabel.grid(sticky="w", row=3, column=0, padx=10, pady=5)

dewEntry = Entry(coolDrinkFrame, font=("arial", 15), bd=7, width=10)
dewEntry.grid(row=3, column=1, padx=10, pady=5)
dewEntry.insert(0, 0)

frootiLabel = Label(
    coolDrinkFrame,
    text="Frooti",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
frootiLabel.grid(sticky="w", row=4, column=0, padx=10, pady=5)

frootiEntry = Entry(coolDrinkFrame, font=("arial", 15), bd=7, width=10)
frootiEntry.grid(row=4, column=1, padx=10, pady=5)
frootiEntry.insert(0, 0)

cocaColaLabel = Label(
    coolDrinkFrame,
    text="Coca Cola",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
cocaColaLabel.grid(sticky="w", row=5, column=0, padx=10, pady=5)

cocaColaEntry = Entry(coolDrinkFrame, font=("arial", 15), bd=7, width=10)
cocaColaEntry.grid(row=5, column=1, padx=10, pady=5)
cocaColaEntry.insert(0, 0)

# Bill Frame

billFrame = Frame(productFrame, bd=8, relief=GROOVE)
billFrame.grid(row=0, column=3, padx=10)

billAreaLabel = Label(
    billFrame,
    text="Bill Area",
    font=("times new roman", 15, "bold"),
    bd=7,
    relief=GROOVE,
)
billAreaLabel.pack(fill=X)

# scroll bar
scrollbar = Scrollbar(billFrame, orient=VERTICAL)
# orient is for we want horizontal or vertical scroll bars
scrollbar.pack(side=RIGHT, fill=Y)

textArea = Text(billFrame, height=17, width=63, yscrollcommand=scrollbar.set)
# yscrollcommand is to move the scrollbar automatically along with content

textArea.pack()
scrollbar.config(command=textArea.yview)
# the above is for upward movement for scrollbar when content is present

# bill menu frame
billmenuFrame = LabelFrame(
    root,
    text="Bill Menu",
    font=("times new roman", 15, "bold"),
    fg="gold",
    bd=8,
    bg="gray20",
    relief=GROOVE,
)
billmenuFrame.pack(fill=X, pady=4)

cosmeticPriceLabel = Label(
    billmenuFrame,
    text="Cosmotic Price",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
cosmeticPriceLabel.grid(sticky="w", row=0, column=0, padx=8, pady=5)

cosmeticPriceEntry = Entry(billmenuFrame, font=("arial", 15), bd=7, width=10)
cosmeticPriceEntry.grid(row=0, column=1, padx=8, pady=5)

groceryPriceLabel = Label(
    billmenuFrame,
    text="Grocery Price",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
groceryPriceLabel.grid(sticky="w", row=1, column=0, padx=8, pady=5)

groceryPriceEntry = Entry(billmenuFrame, font=("arial", 15), bd=7, width=10)
groceryPriceEntry.grid(row=1, column=1, padx=8, pady=5)

coolDrinkPriceLabel = Label(
    billmenuFrame,
    text="Cool Drinks Price",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
coolDrinkPriceLabel.grid(sticky="w", row=2, column=0, padx=8, pady=5)

coolDrinkPriceEntry = Entry(billmenuFrame, font=("arial", 15), bd=7, width=10)
coolDrinkPriceEntry.grid(row=2, column=1, padx=8, pady=5)


cosmeticTaxLabel = Label(
    billmenuFrame,
    text="Cosmotic Tax",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
cosmeticTaxLabel.grid(sticky="w", row=0, column=2, padx=8, pady=5)

cosmeticTaxEntry = Entry(billmenuFrame, font=("arial", 15), bd=7, width=10)
cosmeticTaxEntry.grid(row=0, column=3, padx=8, pady=5)

groceryTaxLabel = Label(
    billmenuFrame,
    text="Grocery Tax",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
groceryTaxLabel.grid(sticky="w", row=1, column=2, padx=8, pady=5)

groceryTaxEntry = Entry(billmenuFrame, font=("arial", 15), bd=7, width=10)
groceryTaxEntry.grid(row=1, column=3, padx=8, pady=5)

coolDrinkTaxLabel = Label(
    billmenuFrame,
    text="Cool Drinks Tax",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
)
coolDrinkTaxLabel.grid(sticky="w", row=2, column=2, padx=8, pady=5)

coolDrinkTaxEntry = Entry(billmenuFrame, font=("arial", 15), bd=7, width=10)
coolDrinkTaxEntry.grid(row=2, column=3, padx=8, pady=5)

# button frame
buttonFrame = Frame(billmenuFrame, bd=8, relief=GROOVE)
buttonFrame.grid(row=0, column=4, rowspan=3, padx=30)

totalBtn = Button(
    buttonFrame,
    text="Total",
    font=("arial", 16, "bold"),
    bg="gray20",
    fg="white",
    bd=5,
    width=8,
    pady=10,
    command=total,
)
""" When using command attribute use functional name only don't put () 
if you do instead of calling the fun after clicking btn
it call when exection it will shows error"""
# when pad is mentioned here instead of grid it is internal pading
totalBtn.grid(row=0, column=0, pady=20, padx=5)

billBtn = Button(
    buttonFrame,
    text="Bill",
    font=("arial", 16, "bold"),
    bg="gray20",
    fg="white",
    bd=5,
    width=8,
    pady=10,
)  # when pad is mentioned here instead of grid it is internal pading
billBtn.grid(row=0, column=1, pady=20, padx=5)

emailBtn = Button(
    buttonFrame,
    text="Email",
    font=("arial", 16, "bold"),
    bg="gray20",
    fg="white",
    bd=5,
    width=8,
    pady=10,
)  # when pad is mentioned here instead of grid it is internal pading
emailBtn.grid(row=0, column=2, pady=20, padx=5)

printBtn = Button(
    buttonFrame,
    text="Print",
    font=("arial", 16, "bold"),
    bg="gray20",
    fg="white",
    bd=5,
    width=8,
    pady=10,
)  # when pad is mentioned here instead of grid it is internal pading
printBtn.grid(row=0, column=3, pady=20, padx=5)

clearBtn = Button(
    buttonFrame,
    text="Print",
    font=("arial", 16, "bold"),
    bg="gray20",
    fg="white",
    bd=5,
    width=8,
    pady=10,
)  # when pad is mentioned here instead of grid it is internal pading
clearBtn.grid(row=0, column=4, pady=20, padx=5)

root.mainloop()  # for window continuously showing
