# Generated by Django 2.1.2 on 2018-10-15 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='name',
            field=models.CharField(choices=[('base1', 'Base'), ('base2', 'Jungle'), ('basep', 'Wizards Black Star Promos'), ('base3', 'Fossil'), ('base4', 'Base Set 2'), ('base5', 'Team Rocket'), ('gym1', 'Gym Heroes'), ('gym2', 'Gym Challenge'), ('neo1', 'Neo Genesis'), ('neo2', 'Neo Discovery'), ('neo3', 'Neo Revelation'), ('neo4', 'Neo Destiny'), ('base6', 'Legendary Collection'), ('ecard1', 'Expedition Base Set'), ('ecard2', 'Aquapolis'), ('ecard3', 'Skyridge'), ('ex1', 'Ruby & Sapphire'), ('ex3', 'Dragon'), ('ex2', 'Sandstorm'), ('ex4', 'Team Magma vs Team Aqua'), ('ex5', 'Hidden Legends'), ('ex6', 'FireRed & LeafGreen'), ('pop1', 'POP Series 1'), ('ex7', 'Team Rocket Returns'), ('ex8', 'Deoxys'), ('ex9', 'Emerald'), ('pop2', 'POP Series 2'), ('ex10', 'Unseen Forces'), ('ex11', 'Delta Species'), ('ex12', 'Legend Maker'), ('pop3', 'POP Series 3'), ('ex13', 'Holon Phantoms'), ('ex14', 'Crystal Guardians'), ('pop4', 'POP Series 4'), ('ex15', 'Dragon Frontiers'), ('ex16', 'Power Keepers'), ('pop5', 'POP Series 5'), ('dp1', 'Diamond & Pearl'), ('dp2', 'Mysterious Treasures'), ('pop6', 'POP Series 6'), ('dp3', 'Secret Wonders'), ('dp4', 'Great Encounters'), ('pop7', 'POP Series 7'), ('dp5', 'Majestic Dawn'), ('dp6', 'Legends Awakened'), ('pop8', 'POP Series 8'), ('dp7', 'Stormfront'), ('pl1', 'Platinum'), ('pop9', 'POP Series 9'), ('pl2', 'Rising Rivals'), ('pl3', 'Supreme Victors'), ('pl4', 'Arceus'), ('hgss1', 'HeartGold & SoulSilver'), ('hgss2', 'HS—Unleashed'), ('hgss3', 'HS—Undaunted'), ('hgss4', 'HS—Triumphant'), ('col1', 'Call of Legends'), ('bwp', 'BW Black Star Promos'), ('bw1', 'Black & White'), ('bw2', 'Emerging Powers'), ('bw3', 'Noble Victories'), ('bw4', 'Next Destinies'), ('bw5', 'Dark Explorers'), ('bw6', 'Dragons Exalted'), ('dv1', 'Dragon Vault'), ('bw7', 'Boundaries Crossed'), ('bw8', 'Plasma Storm'), ('bw9', 'Plasma Freeze'), ('bw10', 'Plasma Blast'), ('xyp', 'XY Black Star Promos'), ('bw11', 'Legendary Treasures'), ('xy0', 'Kalos Starter Set'), ('xy1', 'XY'), ('xy2', 'Flashfire'), ('xy3', 'Furious Fists'), ('xy4', 'Phantom Forces'), ('xy5', 'Primal Clash'), ('dc1', 'Double Crisis'), ('xy6', 'Roaring Skies'), ('xy7', 'Ancient Origins'), ('xy8', 'BREAKthrough'), ('xy9', 'BREAKpoint'), ('g1', 'Generations'), ('xy10', 'Fates Collide'), ('xy11', 'Steam Siege'), ('xy12', 'Evolutions'), ('smp', 'SM Black Star Promos'), ('sm1', 'Sun & Moon'), ('sm2', 'Guardians Rising'), ('sm3', 'Burning Shadows'), ('sm35', 'Shining Legends'), ('sm4', 'Crimson Invasion'), ('sm5', 'Ultra Prism'), ('sm6', 'Forbidden Light'), ('sm7', 'Celestial Storm'), ('sm75', 'Dragon Majesty')], default=('base1', 'Base'), max_length=20, unique=True, verbose_name='name'),
        ),
    ]