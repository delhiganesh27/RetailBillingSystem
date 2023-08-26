from tkinter import *
from tkinter import messagebox
import random
import os, tempfile

# tempfile is an inbuild module to create a temprory files bcs print fun wants a temp file


# functionality part
bill_num = random.randint(1, 9999)
if not os.path.exists("Bills"):
    os.mkdir("Bills")


# Total Function
def total():
    global soap, faceCream, faceWash, hairSpray, hairgel, bodyLotion
    soap = int(bathSoapEntry.get()) * 30
    faceCream = int(faceCreamEntry.get()) * 40
    faceWash = int(faceWashEntry.get()) * 80
    hairSpray = int(hairSprayEntry.get()) * 55
    hairgel = int(hairGelEntry.get()) * 23
    bodyLotion = int(bodyLotionEntry.get()) * 45

    totalCosPrice = float(
        soap + faceCream + faceWash + hairSpray + hairgel + bodyLotion
    )
    cosmeticPriceEntry.delete(0, END)
    cosmeticPriceEntry.insert(0, f"{totalCosPrice:.2f} Rs")
    # 0 indicates index of where to insert
    cosmeticTax = totalCosPrice * 0.15
    cosmeticTaxEntry.delete(0, END)
    cosmeticTaxEntry.insert(0, f"{cosmeticTax:.2f} Rs")

    global rice, oil, daal, wheat, sugar, tea
    rice = int(riceEntry.get()) * 100
    oil = int(oilEntry.get()) * 180
    daal = int(daalEntry.get()) * 150
    wheat = int(wheatEntry.get()) * 120
    sugar = int(sugarEntry.get()) * 200
    tea = int(teaEntry.get()) * 100

    totalGroceryPrice = float(rice + oil + daal + wheat + sugar + tea)
    groceryPriceEntry.delete(0, END)
    groceryPriceEntry.insert(0, f"{totalGroceryPrice:.2f} Rs")
    groceryTax = totalGroceryPrice * 0.05
    groceryTaxEntry.delete(0, END)
    groceryTaxEntry.insert(0, f"{groceryTax:.2f} Rs")

    global maaza, pepsi, sprite, dew, frooti, coke, totalBill
    maaza = int(maazaEntry.get()) * 50
    pepsi = int(pepsiEntry.get()) * 50
    sprite = int(spriteEntry.get()) * 50
    dew = int(dewEntry.get()) * 50
    frooti = int(frootiEntry.get()) * 50
    coke = int(cocaColaEntry.get()) * 50

    totalDrinkPrice = float(maaza + pepsi + sprite + dew + frooti + coke)
    coolDrinkPriceEntry.delete(0, END)
    coolDrinkPriceEntry.insert(0, f"{totalDrinkPrice:.2f} Rs")
    coolDrinkTax = totalDrinkPrice * 0.1
    coolDrinkTaxEntry.delete(0, END)
    coolDrinkTaxEntry.insert(0, f"{coolDrinkTax:.2f} Rs")

    totalBill = (
        totalCosPrice
        + totalDrinkPrice
        + totalGroceryPrice
        + cosmeticTax
        + groceryTax
        + coolDrinkTax
    )


# save function
def saveBill():
    global bill_num
    result = messagebox.askyesno("Confirm", "Do you want to save the bill?")
    if result:
        billContent = textArea.get(1.0, END)
        billFile = open(f"Bills/{bill_num}.txt", "w")
        billFile.write(billContent)
        billFile.close()
        messagebox.showinfo("Success", f"Bill No:{bill_num} is saved successfully!!!")
        bill_num = random.randint(1, 9999)


# Bill function
def bill():
    textArea.delete(1.0, END)
    if nameEntry.get() == "" or phoneEntry.get() == "":
        messagebox.showerror("Error", "Customer details are missing!!!")
    elif (
        cosmeticPriceEntry.get() == ""
        and groceryPriceEntry.get() == ""
        and coolDrinkPriceEntry.get() == ""
    ):
        messagebox.showerror("Error", "No products are selected")
    elif (
        cosmeticPriceEntry.get() == "0 Rs"
        and groceryPriceEntry.get() == "0 Rs"
        and coolDrinkPriceEntry.get() == "0 Rs"
    ):
        messagebox.showerror("Error", "No products are selected")
    else:
        textArea.insert(END, "\t\t*Welcome Customer*")
        textArea.insert(END, f"\nBill Number:{bill_num}")
        textArea.insert(END, f"\nCustomer Name:{nameEntry.get()}")
        textArea.insert(END, f"\nPhone number:+91 {phoneEntry.get()}\n")
        textArea.insert(END, "=" * 63)
        textArea.insert(END, "\n Product\t\t\tQuality\t\t\tPrice\n")
        textArea.insert(END, "=" * 63)
        if bathSoapEntry.get() != "0":
            textArea.insert(
                END, f"\n BathSoap\t\t\t{bathSoapEntry.get()}\t\t\t{soap} Rs"
            )

        if faceCreamEntry.get() != "0":
            textArea.insert(
                END, f"\n Face Cream\t\t\t{faceCreamEntry.get()}\t\t\t{faceCream} Rs"
            )

        if faceWashEntry.get() != "0":
            textArea.insert(
                END, f"\n Face Wash\t\t\t{faceWashEntry.get()}\t\t\t{faceWash} Rs"
            )

        if hairSprayEntry.get() != "0":
            textArea.insert(
                END, f"\n Hair Spray\t\t\t{hairSprayEntry.get()}\t\t\t{hairSpray} Rs"
            )

        if hairGelEntry.get() != "0":
            textArea.insert(
                END, f"\n Hair Gel\t\t\t{hairGelEntry.get()}\t\t\t{hairgel} Rs"
            )

        if bodyLotionEntry.get() != "0":
            textArea.insert(
                END, f"\n Body Lotion\t\t\t{bodyLotionEntry.get()}\t\t\t{bodyLotion} Rs"
            )

        if riceEntry.get() != "0":
            textArea.insert(END, f"\n Rice\t\t\t{riceEntry.get()}\t\t\t{rice} Rs")

        if oilEntry.get() != "0":
            textArea.insert(END, f"\n Oil\t\t\t{oilEntry.get()}\t\t\t{oil} Rs")

        if daalEntry.get() != "0":
            textArea.insert(END, f"\n Daal\t\t\t{daalEntry.get()}\t\t\t{daal} Rs")

        if wheatEntry.get() != "0":
            textArea.insert(END, f"\n Wheat\t\t\t{wheatEntry.get()}\t\t\t{wheat} Rs")

        if sugarEntry.get() != "0":
            textArea.insert(END, f"\n Sugar\t\t\t{sugarEntry.get()}\t\t\t{sugar} Rs")

        if teaEntry.get() != "0":
            textArea.insert(END, f"\n BathSoap\t\t\t{teaEntry.get()}\t\t\t{tea} Rs")

        if maazaEntry.get() != "0":
            textArea.insert(END, f"\n BathSoap\t\t\t{maazaEntry.get()}\t\t\t{maaza} Rs")

        if pepsiEntry.get() != "0":
            textArea.insert(END, f"\n Pepsi\t\t\t{pepsiEntry.get()}\t\t\t{pepsi} Rs")

        if spriteEntry.get() != "0":
            textArea.insert(END, f"\n Sprite\t\t\t{spriteEntry.get()}\t\t\t{sprite} Rs")

        if dewEntry.get() != "0":
            textArea.insert(END, f"\n Dew\t\t\t{dewEntry.get()}\t\t\t{dew} Rs")

        if frootiEntry.get() != "0":
            textArea.insert(END, f"\n Frooti\t\t\t{frootiEntry.get()}\t\t\t{frooti} Rs")

        if cocaColaEntry.get() != "0":
            textArea.insert(
                END, f"\n Coca Cola\t\t\t{cocaColaEntry.get()}\t\t\t{coke} Rs"
            )

        textArea.insert(END, "\n" + "-" * 63)

        if cosmeticTaxEntry.get() != "0.0 Rs":
            textArea.insert(END, f"\n Cosmetic Tax\t\t\t\t\t\t{cosmeticTaxEntry.get()}")

        if groceryTaxEntry.get() != "0.0 Rs":
            textArea.insert(END, f"\n Grocery Tax\t\t\t\t\t\t{groceryTaxEntry.get()}")

        if coolDrinkTaxEntry.get() != "0.0 Rs":
            textArea.insert(
                END, f"\n Cool Drink Tax\t\t\t\t\t\t{coolDrinkTaxEntry.get()}"
            )

        textArea.insert(END, f"\n\n Total\t\t\t\t\t\t{totalBill} Rs\n")

        textArea.insert(END, "-" * 63)

        saveBill()

    # search function


def searchBill():
    for i in os.listdir("Bills/"):
        if i.split(".")[0] == billNumEntry.get():
            file = open(f"Bills/{i}", "r")
            textArea.delete(1.0, END)
            for data in file:
                textArea.insert(END, data)
            file.close()
            break
    else:
        messagebox.showerror("Error", "Invalid bill number")


def printBill():
    if textArea.get(1.0, END) == "\n":  # if there is no content text area is not null
        messagebox.showerror("Error", "Bill is empty")
    else:
        file = tempfile.mktemp(".txt")
        open(file, "w").write(textArea.get(1.0, END))
        os.startfile(file, "print")
        # startfile takes 2 args file and command like print


def send_email():
    if textArea.get(1.0, END) == "\n":  # if there is no content text area is not null
        messagebox.showerror("Error", "Bill is empty")
    else:
        branch1 = Toplevel()  # we may also use Tk()
        branch1.title("Send Email")
        branch1.config(bg="gray20")
        branch1.resizable(0, 0)  # disable the maximization

        senderFrame = LabelFrame(
            branch1,
            text="SENDER",
            font=("arial", 16, "bold"),
            bd=6,
            bg="gray20",
            fg="white",
        )
        senderFrame.grid(row=0, column=0, padx=40, pady=20)

        senderLabel = Label(
            senderFrame,
            text="Sender's Email",
            font=("arial", 14, "bold"),
            bd=6,
            bg="gray20",
            fg="white",
        )
        senderLabel.grid(row=0, column=0, sticky="w")

        senderEntry = Entry(
            senderFrame,
            font=("arial", 14, "bold"),
            bd=6,
            width=23,
            relief=RIDGE,
        )
        senderEntry.grid(row=0, column=1, padx=10, pady=8)

        passwordLabel = Label(
            senderFrame,
            text="Password",
            font=("arial", 14, "bold"),
            bd=6,
            bg="gray20",
            fg="white",
        )
        passwordLabel.grid(row=1, column=0, sticky="w")

        passwordEntry = Entry(
            senderFrame,
            font=("arial", 14, "bold"),
            bd=6,
            width=23,
            relief=RIDGE,
        )
        passwordEntry.grid(row=1, column=1, padx=10, pady=8)

        receiverFrame = LabelFrame(
            branch1,
            text="Recipient",
            font=("arial", 16, "bold"),
            bd=6,
            bg="gray20",
            fg="white",
        )
        receiverFrame.grid(row=1, column=0, padx=40, pady=20)

        receiverLabel = Label(
            receiverFrame,
            text="Email Address",
            font=("arial", 14, "bold"),
            bd=6,
            bg="gray20",
            fg="white",
        )
        receiverLabel.grid(row=0, column=0, sticky="w")

        receiverEntry = Entry(
            receiverFrame,
            font=("arial", 14, "bold"),
            bd=6,
            width=23,
            relief=RIDGE,
        )
        receiverEntry.grid(row=0, column=1, padx=10, pady=8)

        messageLabel = Label(
            receiverFrame,
            text="Message",
            font=("arial", 14, "bold"),
            bd=6,
            bg="gray20",
            fg="white",
        )
        messageLabel.grid(row=1, column=0, sticky="w")

        emailTextArea = Text(
            receiverFrame,
            font=("arial", 14, "bold"),
            bd=2,
            relief=SUNKEN,
            width=42,
            height=11,
        )
        emailTextArea.grid(row=2, column=0, columnspan=2)

        sendBtn = Button(
            branch1, text="SEND", font=("arial", 16, "bold"), width=15, bg="forestgreen"
        )
        sendBtn.grid(row=2, column=0, pady=20)
        branch1.mainloop()


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
    customDeFrame,
    text="SEARCH",
    font=("arial", 12, "bold"),
    bd=7,
    width=10,
    command=searchBill,
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

bathSoapEntry = Entry(cosmeticsFrame, font=("arial", 15), bd=7, width=10)
bathSoapEntry.grid(row=0, column=1, padx=10, pady=5, sticky="w")
bathSoapEntry.insert(
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
buttonFrame.grid(row=0, column=4, rowspan=3, padx=50)

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
    command=bill,
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
    command=send_email,
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
    command=printBill,
    pady=10,
)  # when pad is mentioned here instead of grid it is internal pading
printBtn.grid(row=0, column=3, pady=20, padx=5)

clearBtn = Button(
    buttonFrame,
    text="Clear",
    font=("arial", 16, "bold"),
    bg="gray20",
    fg="white",
    bd=5,
    width=8,
    pady=10,
)  # when pad is mentioned here instead of grid it is internal pading
clearBtn.grid(row=0, column=4, pady=20, padx=5)

root.mainloop()  # for window continuously showing
