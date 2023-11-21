DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS groups;
DROP TABLE IF EXISTS group_members;
DROP TABLE IF EXISTS group_leaders;
DROP TABLE IF EXISTS group_moderators;
DROP TABLE IF EXISTS collect_sessions;
DROP TABLE IF EXISTS collect_session_entries;

CREATE TABLE users (
    username TEXT PRIMARY KEY NOT NULL UNIQUE,
    password TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    date_joined TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE groups (
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    date_created TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    leader TEXT NOT NULL,
    FOREIGN KEY (leader) REFERENCES users (username)
    PRIMARY KEY (name, leader)
);

CREATE TABLE group_moderators (
    group_name TEXT NOT NULL,
    group_leader TEXT NOT NULL,
    moderator TEXT NOT NULL,
    date_added TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (moderator) REFERENCES users (username),
    FOREIGN KEY (group_name, group_leader) REFERENCES groups (name, leader),
    PRIMARY KEY (group_name, group_leader, moderator)
);

CREATE TABLE group_members (
    group_name TEXT NOT NULL,
    group_leader TEXT NOT NULL,
    member TEXT NOT NULL,
    date_added TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (member) REFERENCES users (username),
    FOREIGN KEY (group_name, group_leader) REFERENCES groups (name, leader),
    PRIMARY KEY (group_name, group_leader, member)
);

CREATE TABLE collect_sessions (
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    start_date TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    due_date TEXT NOT NULL,
    group_name TEXT NOT NULL,
    group_leader TEXT NOT NULL,
    FOREIGN KEY (group_leader) REFERENCES users (username),
    FOREIGN KEY (group_name, group_leader) REFERENCES groups (name, leader),
    PRIMARY KEY (name, group_name, group_leader)
);

CREATE TABLE collect_session_entries (
    group_name TEXT NOT NULL,
    group_leader TEXT NOT NULL,
    session_name TEXT NOT NULL,
    member TEXT NOT NULL,
    paid BOOLEAN NOT NULL DEFAULT FALSE,
    date_paid TEXT,
    FOREIGN KEY (group_name, group_leader) REFERENCES groups (name, leader),
    FOREIGN KEY (group_name, group_leader, session_name) REFERENCES collect_sessions (group_name, group_leader, name),
    FOREIGN KEY (group_name, group_leader, member) REFERENCES group_members (group_name, group_leader, member),
    PRIMARY KEY (group_name, group_leader, session_name, member)
);

