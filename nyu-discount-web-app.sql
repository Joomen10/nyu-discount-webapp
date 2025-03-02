CREATE TABLE `users` (
  `user_id` bigint PRIMARY KEY,
  `name` varchar(255),
  `email` varchar(255),
  `address` varchar(255),
  `latitude` decimal,
  `longitude` decimal
);

CREATE TABLE `restaurants` (
  `restaurant_id` bigint PRIMARY KEY,
  `name` varchar(255),
  `address` varchar(255),
  `latitude` decimal,
  `longitude` decimal,
  `rating` decimal,
  `cuisine_type` varchar(255),
  `open_hours` varchar(255),
  `google_place_id` varchar(255),
  `discount_id` bigint
);

CREATE TABLE `menus` (
  `menu_id` bigint PRIMARY KEY,
  `restaurant_id` bigint,
  `name` varchar(255),
  `description` text,
  `price` decimal,
  `category` varchar(255)
);

CREATE TABLE `discounts` (
  `discount_id` bigint PRIMARY KEY,
  `code` varchar(255),
  `discount_type` varchar(255),
  `discount_value` decimal,
  `valid_from` datetime,
  `valid_until` datetime,
  `usage_limit` int
);

CREATE TABLE `reviews` (
  `review_id` bigint PRIMARY KEY,
  `user_id` bigint,
  `restaurant_id` bigint,
  `rating` decimal,
  `comments` text,
  `created_at` datetime
);

ALTER TABLE `restaurants` ADD FOREIGN KEY (`discount_id`) REFERENCES `discounts` (`discount_id`);

ALTER TABLE `menus` ADD FOREIGN KEY (`restaurant_id`) REFERENCES `restaurants` (`restaurant_id`);

ALTER TABLE `reviews` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`);

ALTER TABLE `reviews` ADD FOREIGN KEY (`restaurant_id`) REFERENCES `restaurants` (`restaurant_id`);
