db.createUser(
  {
      user: "tbaum",
      pwd: "testpass",
      roles: [
          {
              role: "readWrite",
              db: "members"
          }
      ]
  }
);