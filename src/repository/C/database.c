#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define DB_FILE "database.dat"
#define CHATS_FILE "chats.dat"
#define MAX_MESSAGES 100
#define MAX_MESSAGE_LENGTH 256

typedef struct {
    char sender[100];
    char message[MAX_MESSAGE_LENGTH];
} Message;

typedef struct {
    int chat_id;
    char participant1[100];
    char participant2[100];
    int message_count;
    Message messages[MAX_MESSAGES];
} Chat;

typedef struct {
    char email[100];
    char name[100];
    char password[100];
    char hash[256];
    char phone[20];
    int message_count;
    char messages[MAX_MESSAGES][MAX_MESSAGE_LENGTH];
} User;

void insert_user(const char* email, const char* name, const char* password, const char* hash, const char* phone) {
    FILE *db = fopen(DB_FILE, "ab+");  // "ab+" cria o arquivo se não existir
    if (db == NULL) {
        printf("Error! Could not open or create database.\n");
        return;
    }

    // Verifica se o usuário já existe
    User user;
    while (fread(&user, sizeof(User), 1, db)) {
        if (strcmp(user.email, email) == 0) {
            printf("Error! Email already exists in the database.\n");
            fclose(db);
            return;
        }
    }

    // Prepara o novo usuário
    memset(&user, 0, sizeof(User));  // Inicializa com zeros para evitar lixo
    strcpy(user.email, email);
    strcpy(user.name, name);
    strcpy(user.password, password);
    strcpy(user.hash, hash);
    strcpy(user.phone, phone);

    // Escreve o usuário no final do arquivo
    fwrite(&user, sizeof(User), 1, db);
    fclose(db);
    printf("User inserted successfully!\n");
}

void get_user(const char* email) {
    FILE *db = fopen(DB_FILE, "rb");
    if (db == NULL) {
        printf("Error! Could not open database for reading.\n");
        return;
    }

    User user;
    memset(&user, 0, sizeof(User));  // Inicializa a estrutura com zeros
    while (fread(&user, sizeof(User), 1, db)) {
        if (strcmp(user.email, email) == 0) {
            printf("Email: %s, Name: %s, Password: %s, Hash: %s, Phone: %s\n",
                   user.email, user.name, user.password, user.hash, user.phone);
            fclose(db);
            return;
        }
    }

    printf("User not found!\n");
    fclose(db);
}

void update_user(const char* email, const char* new_hash) {
    FILE *db = fopen(DB_FILE, "r+b");
    if (db == NULL) {
        printf("Error! Could not open database for updating.\n");
        return;
    }

    User user;
    memset(&user, 0, sizeof(User)); 
    while (fread(&user, sizeof(User), 1, db)) {
        if (strcmp(user.email, email) == 0) {
            strcpy(user.hash, new_hash);
            fseek(db, -(long)sizeof(User), SEEK_CUR);  // Correção aqui
            fwrite(&user, sizeof(User), 1, db);
            fclose(db);
            printf("User hash updated!\n");
            return;
        }
    }

    printf("User not found!\n");
    fclose(db);
}

void delete_user(const char* email) {
    FILE *db = fopen(DB_FILE, "rb");
    FILE *temp = fopen("temp.dat", "wb");
    if (db == NULL || temp == NULL) {
        printf("Error! Could not open files for deletion.\n");
        return;
    }

    User user;
    int found = 0;
    while (fread(&user, sizeof(User), 1, db)) {
        if (strcmp(user.email, email) == 0) {
            found = 1;
            continue;
        }
        fwrite(&user, sizeof(User), 1, temp);
    }

    fclose(db);
    fclose(temp);
    remove(DB_FILE);
    rename("temp.dat", DB_FILE);

    if (found) {
        printf("User deleted successfully!\n");
    } else {
        printf("User not found!\n");
    }
}

void list_users(char *buffer, size_t buffer_size) {
    FILE *db = fopen(DB_FILE, "rb");
    if (db == NULL) {
        snprintf(buffer, buffer_size, "Error! Could not open database for reading.\n");
        return;
    }

    User user;
    buffer[0] = '\0';  // Inicializa o buffer vazio

    while (fread(&user, sizeof(User), 1, db)) {
        if (strlen(user.email) == 0) continue;  // Ignora registros inválidos

        char temp[512];
        snprintf(temp, sizeof(temp), "%s|%s|%s|%s|%s\n",
                 user.email, user.name, user.password, user.hash, user.phone);

        if (strlen(buffer) + strlen(temp) < buffer_size) {
            strcat(buffer, temp);
        } else {
            break;
        }
    }

    if (strlen(buffer) == 0) {
        snprintf(buffer, buffer_size, "No users found in the database.\n");
    }

    fclose(db);
}

void send_message(const char* sender_email, const char* recipient_email, const char* message) {
    FILE *chats_db = fopen(CHATS_FILE, "r+b");
    if (chats_db == NULL) {
        chats_db = fopen(CHATS_FILE, "wb+");
        if (chats_db == NULL) {
            printf("Error! Could not open chat database.\n");
            return;
        }
    }

    Chat chat;
    int chat_found = 0;
    int last_chat_id = 0;
    long position = 0;

    while (fread(&chat, sizeof(Chat), 1, chats_db)) {
        if ((strcmp(chat.participant1, sender_email) == 0 && strcmp(chat.participant2, recipient_email) == 0) ||
            (strcmp(chat.participant1, recipient_email) == 0 && strcmp(chat.participant2, sender_email) == 0)) {
            chat_found = 1;
            position = ftell(chats_db) - sizeof(Chat);
            break;
        }
        if (chat.chat_id > last_chat_id) {
            last_chat_id = chat.chat_id;
        }
    }

    if (!chat_found) {
        memset(&chat, 0, sizeof(Chat));
        chat.chat_id = last_chat_id + 1;
        strcpy(chat.participant1, sender_email);
        strcpy(chat.participant2, recipient_email);
    }

    if (chat.message_count >= MAX_MESSAGES) {
        printf("Error! Chat message limit reached.\n");
        fclose(chats_db);
        return;
    }

    strcpy(chat.messages[chat.message_count].sender, sender_email);
    strcpy(chat.messages[chat.message_count].message, message);
    chat.message_count++;

    if (chat_found) {
        fseek(chats_db, position, SEEK_SET);
    } else {
        fseek(chats_db, 0, SEEK_END);
    }
    fwrite(&chat, sizeof(Chat), 1, chats_db);

    fclose(chats_db);
    printf("Message sent successfully!\n");
}

void list_chats(const char* email, char *buffer, size_t buffer_size) {
    FILE *chats_db = fopen(CHATS_FILE, "rb");
    if (chats_db == NULL) {
        snprintf(buffer, buffer_size, "Error! Could not open chat database.\n");
        return;
    }

    Chat chat;
    buffer[0] = '\0';  // Inicializa o buffer vazio
    char temp[256];
    
    while (fread(&chat, sizeof(Chat), 1, chats_db)) {
        if (strcmp(chat.participant1, email) == 0 || strcmp(chat.participant2, email) == 0) {
            snprintf(temp, sizeof(temp), "%d|%s\n", 
                     chat.chat_id, 
                     strcmp(chat.participant1, email) == 0 ? chat.participant2 : chat.participant1);
            
            if (strlen(buffer) + strlen(temp) < buffer_size) {
                strcat(buffer, temp);
            } else {
                break;
            }
        }
    }

    if (strlen(buffer) == 0) {
        snprintf(buffer, buffer_size, "No chats found.\n");
    }

    fclose(chats_db);
}

void list_messages_from_chat(int chat_id, char *buffer, size_t buffer_size) {
    FILE *chats_db = fopen(CHATS_FILE, "rb");
    if (chats_db == NULL) {
        snprintf(buffer, buffer_size, "Error! Could not open chat database.\n");
        return;
    }

    Chat chat;
    buffer[0] = '\0';  // Inicializa o buffer vazio
    char temp[512];

    while (fread(&chat, sizeof(Chat), 1, chats_db)) {
        if (chat.chat_id == chat_id) {
            for (int i = 0; i < chat.message_count; i++) {
                snprintf(temp, sizeof(temp), "%s|%s\n",
                         chat.messages[i].sender,
                         chat.messages[i].message);

                if (strlen(buffer) + strlen(temp) < buffer_size) {
                    strcat(buffer, temp);
                } else {
                    break;
                }
            }
            fclose(chats_db);
            return;
        }
    }

    snprintf(buffer, buffer_size, "Chat ID not found.\n");
    fclose(chats_db);
}

void list_messages(const char* email) {
    FILE *db = fopen(DB_FILE, "rb");
    if (db == NULL) {
        printf("Error! Could not open database for reading messages.\n");
        return;
    }

    User user;
    while (fread(&user, sizeof(User), 1, db)) {
        if (strcmp(user.email, email) == 0) {
            printf("Messages for %s:\n", email);
            if (user.message_count == 0) {
                printf("No messages found.\n");
            } else {
                for (int i = 0; i < user.message_count; i++) {
                    printf("%d: %s\n", i + 1, user.messages[i]);
                }
            }
            fclose(db);
            return;
        }
    }

    printf("Error! User not found.\n");
    fclose(db);
}
