from project.influencers.base_influencer import BaseInfluencer
from project.campaigns.base_campaign import BaseCampaign


class StandardInfluencer(BaseInfluencer):
    INITIAL_PAYMENT_PERCENTAGE = 0.45       # 45%

    CAMPAIGNS = {
        "HighBudgetCampaign": 1.2,
        "LowBudgetCampaign": 0.9
    }

    def calculate_payment(self, campaign: BaseCampaign):
        payment = campaign.budget * StandardInfluencer.INITIAL_PAYMENT_PERCENTAGE
        return payment

    def reached_followers(self, campaign_type: str):
        reached_followers = self.followers * self.engagement_rate * StandardInfluencer.CAMPAIGNS[campaign_type]
        return reached_followers