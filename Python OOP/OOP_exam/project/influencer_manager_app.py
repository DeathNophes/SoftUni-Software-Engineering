from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer


class InfluencerManagerApp:
    VALID_INFLUENCER_TYPES = {
        "PremiumInfluencer": PremiumInfluencer,
        "StandardInfluencer": StandardInfluencer
    }

    VALID_CAMPAIGNS = {
        "HighBudgetCampaign": HighBudgetCampaign,
        "LowBudgetCampaign": LowBudgetCampaign
    }

    def __init__(self):
        self.influencers = []
        self.campaigns = []

    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float):
        try:
            influencer = self.VALID_INFLUENCER_TYPES[influencer_type](username, followers, engagement_rate)
        except KeyError:
            return f"{influencer_type} is not an allowed influencer type."

        for infl in self.influencers:
            if infl.username == username:
                return f"{username} is already registered."

        self.influencers.append(influencer)
        return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):
        if campaign_type not in self.VALID_CAMPAIGNS.keys():
            return f"{campaign_type} is not a valid campaign type."

        for camp in self.campaigns:
            if camp.campaign_id == campaign_id:
                return f"Campaign ID {campaign_id} has already been created."

        campaign = self.VALID_CAMPAIGNS[campaign_type](campaign_id, brand, required_engagement)

        self.campaigns.append(campaign)
        return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."

    def participate_in_campaign(self, influencer_username: str, campaign_id: int):
        influencer = [i for i in self.influencers if i.username == influencer_username]
        campaign = [c for c in self.campaigns if c.campaign_id == campaign_id]

        if not influencer:
            return f"Influencer '{influencer_username}' not found."

        if not campaign:
            return f"Campaign with ID {campaign_id} not found."

        if not campaign[0].check_eligibility(influencer[0].engagement_rate):
            return f"Influencer '{influencer_username}' does not meet the eligibility criteria " + \
                   f"for the campaign with ID {campaign_id}."

        influencer_payment = influencer[0].calculate_payment(campaign[0])

        if influencer_payment > 0.0:
            campaign[0].approved_influencers.append(influencer[0])
            campaign[0].budget -= influencer_payment
            influencer[0].campaigns_participated.append(campaign[0])

            return f"Influencer '{influencer_username}' has successfully participated " + \
                f"in the campaign with ID {campaign_id}."

    def calculate_total_reached_followers(self):
        result = {}

        for campaign in self.campaigns:
            if campaign.approved_influencers:
                influencers = campaign.approved_influencers

                total_followers = sum([
                    influencer.reached_followers(campaign.__class__.__name__) for influencer in influencers
                ])

                if total_followers > 0:
                    result[campaign] = total_followers

        return result

    def influencer_campaign_report(self, username: str):
        influencer = [i for i in self.influencers if i.username == username][0]

        result = influencer.display_campaigns_participated()

        return result

    def campaign_statistics(self):
        sorted_campaigns = sorted(
            self.campaigns,
            key=lambda c: (len(c.approved_influencers), -c.budget)
        )

        result = f"$$ Campaign Statistics $$\n"

        for camp in sorted_campaigns:
            total_reached_followers = 0

            for infl in camp.approved_influencers:
                total_reached_followers += infl.reached_followers(camp.__class__.__name__)

            result += f"  * Brand: {camp.brand}, " + \
                      f"Total influencers: {len(camp.approved_influencers)}, " + \
                      f"Total budget: ${camp.budget:.2f}, " + \
                      f"Total reached followers: {total_reached_followers:.0f}\n"

        return result[:-1]
