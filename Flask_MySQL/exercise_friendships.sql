SELECT * FROM users
LEFT JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users as users2 ON friend.id = users2.id