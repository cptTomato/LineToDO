import typer


app = typer.Typer()
import terminaltables


@app.command()
def add():
   job = input ("Was ist zu tun: ")
   daten= open('Datenbank.txt', 'a') 
   daten.writelines(job + '\n')
   daten.close()


@app.command()
def done():
   jobDone = str(input("Welches Element ist erledigt? "))
   daten = open('Datenbank.txt', 'r') 
   lines = daten.readlines()

   datenW = open('Datenbank.txt', 'w') 

   for line in lines:
        if line.find(jobDone):
            print(line)
            print(jobDone)
            datenW.write(line)
   daten.close()

@app.command()
def tabelle():
   header = "Job"
   data = [
   [header]]
   daten = open('Datenbank.txt', 'r')
   for i in daten: 
      data.append([i])
   table = terminaltables.AsciiTable(data)
   print(table.table)


if __name__ == "__main__":
    app()