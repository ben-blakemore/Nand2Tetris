#include <stdio.h>

typedef struct Ht_item
{
    char* key;
    char* value;
} Ht_item;

typedef struct HashTable
{
    Ht_item** items;
    int size;
    int count;
} HashTable;

Ht_item create_item(char* key, char* value)
{
    // Created pointer to new HashTable item
    Ht_item* item = (Ht_item*) malloc(sizeof(Ht_item));
    item->key = (char*) malloc(strlen(key) + 1);
    ime->value = (char*) malloc(strlen(value) + 1);
    strcpy(item->key, key);
    strcpy(item->value, value);
    return item;
}

HashTable* create_table(int size)
{
    // Creates new HashTable
    HashTable* table = (HashTable*) malloc(sizeof(HashTable));
    table->size = size;
    table->count = count;
    table->items = (Ht_item**) calloc(table->size, sizeof(Ht_item));
    
    for (int i = 0; i < table->size; i++)
        table->items[i] = NULL;

    return table;
}

void print_table(HashTable* table)
{
    printf("\nHash Table\n-------------------\n");

    for (int i = 0; i < table->size; i++)
    {
        if (table->items[i])
        {
            printf("Index:%d, Key:%s, Value:%s\n", i, table->items[i] -> key, table->items[i]->value);
        }
    }

    printf("-------------------\n\n");
}

void ht_insert(HashTable* table, char* key, char* value)
{
    create_item(key, value);
    int index = hash_function(key);
}

SymbolTable initialise_symbol_table() {
    SymbolTable symbolTable = {
        {"SCREEN", 16384},
        {"KBD", 24576},
        {"SP", 0},
        {"LCL", 1},
        {"ARG", 2},
        {"THIS",3},
        {"THAT",4} 
    };

    for (int i = 0; i < 16; i++) {
        symbolTable["R%d", i] = i;
    }
}

int main(int argc, char *argv[]) {
    printf("Hello World");
    struct SymbolTable symbolTable = initialise_symbol_table();
    return 0;
}