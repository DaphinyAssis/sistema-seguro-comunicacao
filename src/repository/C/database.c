#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define DB_FILE "database.dat"

typedef struct {
    char email[100];
    char name[100];
    char password[100];
    char hash[256];
    char phone[20];
} User;

void insert_user(const char* email, const char* name, const char* password, const char* hash, const char* phone) {
    FILE *db = fopen(DB_FILE, "ab");
    if (db == NULL) {
        printf("Error! Could not open database for writing.\n");
        return;
    }

    User user;
    strcpy(user.email, email);
    strcpy(user.name, name);
    strcpy(user.password, password);
    strcpy(user.hash, hash);
    strcpy(user.phone, phone);

    fwrite(&user, sizeof(User), 1, db);
    fclose(db);
}

void get_user(const char* email) {
    FILE *db = fopen(DB_FILE, "rb");
    if (db == NULL) {
        printf("Error! Could not open database for reading.\n");
        return;
    }

    User user;
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
        char temp[512];
        snprintf(temp, sizeof(temp), "Email: %s, Name: %s, Password: %s, Hash: %s, Phone: %s\n",
                 user.email, user.name, user.password, user.hash, user.phone);
        
        // Verifica se ainda há espaço no buffer antes de concatenar
        if (strlen(buffer) + strlen(temp) < buffer_size) {
            strcat(buffer, temp);
        } else {
            break;  // Evita estouro do buffer
        }
    }

    if (strlen(buffer) == 0) {
        snprintf(buffer, buffer_size, "No users found in the database.\n");
    }

    fclose(db);
}

