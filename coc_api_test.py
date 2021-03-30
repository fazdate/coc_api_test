import coc

with open("credentials.txt") as file:
    adatok = file.readlines()
cred = [x.strip() for x in adatok] 


client = coc.login(cred[0], cred[1])
player_tag = cred[2]
clan_tag = cred[3]

async def main():
    # Ha van megadva player tag    
    if player_tag:
        player = await client.get_player(player_tag)
        print("Játékos neve: " + str(player))

        player_clan = await player.get_detailed_clan()
        print("Játékos klánja: " + str(player_clan))

        print("A játékos hősei: ") 
        for hero in player.heroes:
            print("{}: Lv {}/{}\n".format(str(hero), hero.level, hero.max_level))

        print()

    # Ha van megadva clan tag
    if clan_tag:
        clan = await client.get_clan(clan_tag)
        print("A keresett klán tagjai: ")
        async for player in clan.get_detailed_members():
            print(player.name)
        
    
client.loop.run_until_complete(main())
client.close()