import discodip as dip
import logintoken as tokens

connection = dip.Discodip(tokens.get_token())
connection.run()