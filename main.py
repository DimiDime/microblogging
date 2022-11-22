from website import create_app # Can Import everything in website folder

app = create_app()

if __name__ == '__main__': # Only if we run this file 
  app.run(debug=True)      # Execute this line