import qrcode as qr


scan = qr.make("https://musaif.netlify.com")
scan.save("Musaif_portfolio.png")