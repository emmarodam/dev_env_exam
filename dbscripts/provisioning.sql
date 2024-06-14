DROP TABLE IF EXISTS coffee_beans;

CREATE TABLE coffee_beans (
    id SERIAL PRIMARY KEY,
    title VARCHAR(50),
    description TEXT,
    price INTEGER
);

INSERT INTO coffee_beans (title, description, price)
VALUES
    ('Arabica', 'Arabica beans are known for their smooth and mild flavor profile with subtle acidity. They often have floral and fruity notes, making them popular for specialty coffees.', 20),
    ('Robusta', 'Robusta beans have a stronger, more robust flavor compared to Arabica beans. They are often higher in caffeine content and have a more bitter taste with earthy and woody notes.', 15),
    ('Ethiopian Yirgacheffe', 'These beans are known for their bright acidity, floral aroma, and fruity flavor notes. Ethiopian Yirgacheffe is prized for its complex and vibrant taste profile.', 25);
