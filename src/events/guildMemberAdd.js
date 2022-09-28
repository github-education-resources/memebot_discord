import { EmbedBuilder, userMention } from "discord.js";
import axios from "axios";

const CHANNEL_NAME = process.env.CHANNEL_NAME;
const MEME_API = process.env.MEME_API_URL;

const event = {
  name: "guildMemberAdd",
  async execute(member) {
    const channel = member.guild.channels.cache.find(
      (channel) => channel.name === CHANNEL_NAME
    );

    const welcomeMessage = await getWelcomeMessageWithMeme(member.id);
    channel.send(welcomeMessage);
  },
};

// this function returns a welcome message.
const getWelcomeMessage = (userId) => {
  return { content: `Welcome to the server, ${userMention(userId)}!` };
};

// this function returns a welcome message with a meme.
const getWelcomeMessageWithMeme = async (userId) => {
  const meme = await getMeme();

  return {
    content: `Welcome to the server, ${userMention(userId)}!
    Here's a meme for you!`,
    embeds: [meme],
  };
};

const getMeme = async () => {
  const response = await axios.get(MEME_API);
  return new EmbedBuilder().setImage(response.data.url);
};

export default event;
